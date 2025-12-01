
import ads


if __name__=='__main__':
   import os
   import argparse

   ads.config.token = os.environ.get('ADS_DEV_KEY')

   parser = argparse.ArgumentParser(
                    prog='program_publication_statistics',
                    description='Given a NASA award or proposal number, this retrieves the publications that appear in ADS with taht proposal number in the acknowledgement.  This can also produce the number of publications by being provided a file of award or proposal numbers.  This needs to be run with either an award number of filename argument specified.')
   parser.add_argument('-a', '--award', type=str, default=None, help='Award or proposal number')
   parser.add_argument('-f', '--filename', default=None, help='File that is a list of awards or proposal numbers')
   args = parser.parse_args()
 

   if args.filename == None:
      print(f"ack:{args.award}")
      papers = ads.SearchQuery(q=f"ack:{args.award}", fl=["title", 'pub', 'property'])
      for paper in papers:
          print(paper.title, paper.pub, paper.property)
   else:
      with open(args.filename, 'r') as file:
           awards = file.readlines()

      for award in awards:
          print(award)
          papers = ads.SearchQuery(q=f"ack:{award}")
          for paper in papers:
              print(paper.title)
