HHA507_APIs
 To perform a GET request, 
 documentation (found here: https://arxiv.org/help/api/user-manual) says that 
 the url that can be used is in the form 
 http://export.arxiv.org/api/{method_name}?{parameters}. Here, the method_name=query 
 and multiple parameteres can be defined. 
 Within the parameters there are 4 main ones; search_query is a string (str) which defines the topic. id_list is a comma-delimited str, start is an integer (int) which defaults as 0 and max_results which is also an integer(int) and defaults as 0 unless specified.