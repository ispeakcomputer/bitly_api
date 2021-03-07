from bitly import Bitly

# group = bitly_object.group_getter() 
# Get the links for the users groups
# group_links = bitly_object.bitlink_getter(group['default_group_guid'])

#Feed in the bitly data on a user groups links to pull metrics and convert to 30 day avg 
class Helper:

    def json_snippet_builder(self, group_links):
        bitly_object = Bitly()
    
        for link in group_links['links']:
            metrics_from_bitly = bitly_object.clicks_getter(link['id'])
            
            links = []
            one_link_metrics = {}            
            one_link_metrics['metrics']=metrics_from_bitly['metrics']
            one_link_metrics['bitlink']=link['id']
            
            links.append(one_link_metrics)
        
        return links
    def avg_calculator(self, links):
        for bitlink_data in links:
            bitlink_avgs = []
            one_bitlink_data = {}
            one_bitlink_data['bitlink'] = bitlink_data['bitlink']
            one_bitlink_data['avgs'] = []
            for data in bitlink_data['metrics']:
                bitlink_avg = {}
                bitlink_avg['country'] = data['value']
                # clicks/30 days for 30 day avgerage
                bitlink_avg['30_day_avg'] = data['clicks']/30
        
                one_bitlink_data['avgs'].append(bitlink_avg)
                #print(bitlink_avg)
        return one_bitlink_data
