import argparse
import datetime
import json
import os
import staticjinja

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument(
        "--config",
        dest="config_file_name",
        metavar="FILE",
        type=str,
    )

    args = args_parser.parse_args()

    output_dir = os.path.abspath(os.path.join(os.getcwd(), "deploy"))
    if args.config_file_name:
        with open(args.config_file_name) as json_file:  
            config = json.load(json_file)
    else:
        config = {
            "base_url": "file://" + output_dir,
            "google_api_key": "XXX-GOOGLE-API_KEY",
            "analytics_id": "UA-27729857-6",
        }

    site = staticjinja.Site.make_site(outpath=output_dir, env_globals=config)
    site.render()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")

    with open(os.path.join(output_dir, "sitemap.xml"), "w") as sitemap_file:
        sitemap_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        sitemap_file.write('<urlset\n')
        sitemap_file.write('    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n')
        sitemap_file.write('    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n')
        sitemap_file.write('    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n')
        for root, subdirs, files in os.walk(output_dir):
            for file_name in files:
                if not file_name.endswith('.html'):
                    continue
                print(f'{root} {file_name}')
                path = os.path.relpath(root, output_dir)
                if path == '.':
                    url = config["base_url"] + "/" + file_name
                else:
                    url = config["base_url"] + "/" + path + "/" + file_name
            sitemap_file.write('<url>\n')
            sitemap_file.write(f'    <loc>{url}</loc>\n')
            sitemap_file.write(f'    <lastmod>{timestamp}</lastmod>\n')
            sitemap_file.write(f'    <changefreq>monthly</changefreq>\n')
            sitemap_file.write('</url>\n')
        sitemap_file.write('</urlset>\n')
