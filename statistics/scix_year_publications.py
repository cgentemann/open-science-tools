
import ads


if __name__=='__main__':
   import os
   import argparse

   ads.config.token = os.environ.get('ADS_DEV_KEY')

   parser = argparse.ArgumentParser(
                    prog='scix_year_publications',
                    description='Given a year, print a list of refrerreed publications from that year that have "supported by NASA" in the Acknowledgements')
   parser.add_argument('year')
   args = parser.parse_args()
 
   return_format = ['title', 'pub', 'property', 'bibcode']
   rows = 2000
   start = 0
   while True:
      papers = ads.SearchQuery(q=f"year:{args.year} property:refereed full:'supported by NASA'", fl=return_format, rows=rows, start=start)

      try:
         for paper in papers:
          openaccess = str("OPENACCESS" in paper.property)
          print(paper.title[0] +'; ' + paper.pub + "; " +  openaccess + "; " + paper.bibcode) #paper.property)
      except:
         break
      start = start + rows
