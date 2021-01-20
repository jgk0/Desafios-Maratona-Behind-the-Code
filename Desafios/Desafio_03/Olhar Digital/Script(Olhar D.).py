import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_urls = ["https://olhardigital.com.br/colunistas/wagner_sanchez/post/o_futuro_cada_vez_mais_perto/78972" ,"https://olhardigital.com.br/colunistas/wagner_sanchez/post/os_riscos_do_machine_learning/80584" ,"https://olhardigital.com.br/ciencia-e-espaco/noticia/nova-teoria-diz-que-passado-presente-e-futuro-coexistem/97786" ,"https://olhardigital.com.br/noticia/inteligencia-artificial-da-ibm-consegue-prever-cancer-de-mama/87030" ,"https://olhardigital.com.br/ciencia-e-espaco/noticia/inteligencia-artificial-ajuda-a-nasa-a-projetar-novos-trajes-espaciais/102772" ,"https://olhardigital.com.br/colunistas/jorge_vargas_neto/post/como_a_inteligencia_artificial_pode_mudar_o_cenario_de_oferta_de_credito/78999" ,"https://olhardigital.com.br/ciencia-e-espaco/noticia/cientistas-criam-programa-poderoso-que-aprimora-deteccao-de-galaxias/100683"]
for i in my_urls:
    uClient = uReq(my_urls[my_urls.index(i)])
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    author = page_soup.find("meta", {"name":"author"})["content"]
    if (author == 'Redação Olhar Digital'):
        author = author.replace('Redação Olhar Digital', 'Wagner Sanchez')
    body = page_soup.find("div", {"class":"mat-header"}).h2.text + page_soup.find("div", {"class":"mat-txt"}).text 
    title = page_soup.find("title").text
    aux = body
    aux2 = ''
    aux2 = aux.replace('\t', '')
    aux2 = aux2.replace('\n\n', '\\n\\n')
    aux2 = aux2.replace('\n', '\\n')
    aux2 = aux2.replace('"', '\\"')
    f =  open ('Olhar Digital ' + str(my_urls.index(i)) + '.json', 'w', encoding="utf8")
    f.write('{\n\t"title": "'+title+'",\n\t"author": "'+author+'",\n\t"body": "'+aux2+'",\n\t"type": "article",\n\t"url": "'+i+'"\n}')
    f.close()





