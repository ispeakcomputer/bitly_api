from bitly import Bitly


class Helper:
    def __init__(self, token):
        self.token = token

    def json_snippet_builder(self, group_links):
        #Create our own json from Bitly API data to feed into avg_calculator
        bitly_object = Bitly(self.token)
        
        links = []
        for link in group_links['links']:
            metrics_from_bitly = bitly_object.clicks_getter(link['id'])
            # links = []
            one_link_metrics = {}            
            one_link_metrics['metrics']=metrics_from_bitly['metrics']
            one_link_metrics['bitlink']=link['id']
            
            links.append(one_link_metrics)
            # print(links)        
        return links
    def avg_calculator(self, links):
        # 1.) build this JSON for ea bitlink in "links" -> 
        # {"bitlink": "bit.ly/test", "avgs": []}
        links_json={}
        links_list=[]
        for bitlink_data in links:
            one_bitlink_data = {}
            one_bitlink_data['bitlink'] = bitlink_data['bitlink']
            one_bitlink_data['avgs'] = []
            # 2.) Run calculation for each country and build JSON->
            # {"country": "US", "30_day_avg": 23.733333333333334}
            for data in bitlink_data['metrics']:
                bitlink_avg = {}
                bitlink_avg['country'] = data['value']
                # clicks divided by 30 = 30 day average
                bitlink_avg['30_day_avg'] = data['clicks']/30
        
                # 3.) add 2.) data to 1.) "avgs" list
                one_bitlink_data['avgs'].append(bitlink_avg)
            links_list.append(one_bitlink_data)
            # print(links_list)
        return links_list
