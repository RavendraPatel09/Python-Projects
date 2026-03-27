url = input("Enter a URL: ")#Code to parse a URL into protocol, domain, and page
protocol = url.find("://") #find the position of "://"
dot1 = url.find(".")#find the position of first "."
dot2 = url.rfind(".",dot1+1)#find the position of last "."
domain = url[dot1+1:dot2]#extract domain
page=url[dot2+1:]   #extract page
print("Protocol: ",url)
print("Domain: ",domain)
print("Page: ",page)
#https://ibm-learning.udemy.com/course/learn-python-with-abdul-bari/learn/lecture/31801590#overview
#output
#Enter a URL: https://ibm-learning.udemy.com/course/learn-python-with-abdul-bari/learn/lecture/31801590#overview
#Protocol:  https://ibm-learning.udemy.com/course/learn-python-with-abdul-bari/learn/lecture/31801590#overview
#Domain:  ibm-learning.udemy
#Page:  com/course/learn-python-with-abdul-bari/learn/lecture/31801590#overview 