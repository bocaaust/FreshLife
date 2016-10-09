import urllib
import untangle
import xmltodict

query = "http://www.SupermarketAPI.com/api.asmx/COMMERCIAL_SearchByProductName?APIKEY=c9c2055184&ItemName="

def Fetch_Price( prod_name ):
    new_query = query + urllib.parse.quote(prod_name)
    content = urllib.request.urlopen(new_query).read()
    content = str(content)
    content1 = content[2:-1].rstrip("\\r\\n")
    content2 = content1.replace("\\r\\n","")
    obj_dict = xmltodict.parse(content2)
    res = obj_dict['ArrayOfProduct_Commercial']['Product_Commercial'][0]['Pricing']
    print(res)
    return res

#Fetch_Price( "7 Grain Whole Wheat Bread" )
