import scrapy
import csv
import unidecode


class WestbengalSpider(scrapy.Spider):
    name = 'westbengal'
    allowed_domains = ["myneta.info"]
    start_urls = ['https://myneta.info/westbengal2016/index.php?action=summary&subAction=winner_women&sort=candidate#summary']

    def parse(self, response):
        DELIM = ","

        def clean_row(row):
            return [item.strip().replace(DELIM, "") if item else "" for item in row]
        
        rows = response.css("tr")
        with open(f"wbwomen2016.csv", "w", newline="") as f:
            writer = csv.writer(f, delimiter = DELIM)
            #data1 = [
                    #unidecode.unidecode(word) for word in row.css("tr *::text").getall()
                    #word for word in row.css("td *::text").getall()
                #]
            #if len(data1) == 11:
                    #writer.writerow(clean_row(data1[:-1]))
            #writer = csv.writer(f, delimiter = DELIM)
            for row in rows:
                #heading = [
                    #unidecode.unidecode(word) for word in row.css("th *::text").getall()
                #]
                data = [
                    unidecode.unidecode(word) for word in row.css("td *::text").getall()
                    #word for word in row.css("td *::text").getall()
                ]
                #if len(heading) == 9:
                    #writer.writerow(clean_row(data[:-1]))
                if len(data) == 11:
                    writer.writerow(clean_row(data[:-1]))

                    #[word.replace("\xa0"," ") for word in row.css("td *::text").getall()]
                
        #the star is for getting the criminal records that are in red    
        #print(table)
        #print("\n\n\n\n")