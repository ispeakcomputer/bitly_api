from bitly import Bitly


class Helper:
    def __init__(self, token):
        self.token = token

    def json_snippet_builder(self, group_links):
        bitly_object = Bitly(self.token)
        
        links = []
        for link in group_links['links']:
            metrics_from_bitly = bitly_object.clicks_getter(link['id'])
            one_link_metrics = {}            
            one_link_metrics['metrics']=metrics_from_bitly['metrics']
            one_link_metrics['bitlink']=link['id']
            
            links.append(one_link_metrics)
        return links
    def avg_calculator(self, links):
        links_json={}
        links_list=[]
        for bitlink_data in links:
            one_bitlink_data = {}
            one_bitlink_data['bitlink'] = bitlink_data['bitlink']
            one_bitlink_data['avgs'] = []
            for data in bitlink_data['metrics']:
                bitlink_avg = {}
                bitlink_avg['country'] = data['value']
                bitlink_avg['30_day_avg'] = data['clicks']/30
                one_bitlink_data['avgs'].append(bitlink_avg)
            links_list.append(one_bitlink_data)
        return links_list
