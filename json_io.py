import  json

def json_getter(j_string, tag):
  j_dic = json.loads(j_string)
  for child in j_dic:
    if(child == tag):
      return j_dic[child]
    else:
      for x in j_dic[child]:
        if(x == tag):
          return j_dic[child][x]
           
def json_setter(j_string, tag, entry):
  j_dic = json.loads(j_string)
  for child in j_dic:
    if(child == tag):
      j_dic[child] = entry
      return json.dumps(j_dic)
    else:
      for x in j_dic[child]:
        if(x == tag):
          j_dic[child][x] = entry
          return json.dumps(j_dic)
      
'''
#Example usage      
EMPTY_CONFIG_XML = json_setter(Example_json, 'method', 'new')      
print json_getter(Example_json, 'method')

#Example json string
Example_json = '{
	"$schema": "http://json-schema.org/draft-04/schema#",
	"title": "Request information",
	"type": "object",
	"description": "Information necessary to access project sources on github repository and method to be applied",
	"properties": {
		"object_type": {
			"type": "string"
		},
		"github_login": {
			"type": "string"
		},
		"github_password": {
			"type": "string"
		},
		"card_id": {
			"type": "string"
		},
		"repository_url": {
			"type": "string"
		},
		"project_name": {
			"type": "string"
		},
		"method": {
			"type": "string"
		}
	}
}'   
'''
