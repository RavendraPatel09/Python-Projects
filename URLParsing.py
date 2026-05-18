url = input("Enter a URL: ")#Code to parse a URL into protocol, domain, and page
protocol = url.find("://") #find the position of "://"
dot1 = url.find(".")#find the position of first "."
dot2 = url.rfind(".",dot1+1)#find the position of last "."
domain = url[dot1+1:dot2]
page=url[dot2+1:]  
print("Protocol: ",url)
print("Domain: ",domain)
print("Page: ",page)
