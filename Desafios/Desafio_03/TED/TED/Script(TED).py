import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_urls = ['https://www.ted.com/talks/helen_czerski_the_fascinating_physics_of_everyday_life/transcript?language=pt-br#t-81674', 'https://www.ted.com/talks/kevin_kelly_how_ai_can_bring_on_a_second_industrial_revolution/transcript?language=pt-br', 'https://www.ted.com/talks/sarah_parcak_help_discover_ancient_ruins_before_it_s_too_late/transcript?language=pt-br', 'https://www.ted.com/talks/sylvain_duranton_how_humans_and_ai_can_work_together_to_create_better_businesses/transcript?language=pt-br', 'https://www.ted.com/talks/chieko_asakawa_how_new_technology_helps_blind_people_explore_the_world/transcript?language=pt-br', 'https://www.ted.com/talks/pierre_barreau_how_ai_could_compose_a_personalized_soundtrack_to_your_life/transcript?language=pt-br', 'https://www.ted.com/talks/tom_gruber_how_ai_can_enhance_our_memory_work_and_social_lives/transcript?language=pt-br']
for i in my_urls:
    uClient = uReq(my_urls[my_urls.index(i)])
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    author = page_soup.find("meta",{"name":"author"})["content"]
    bodys = page_soup.findAll("div", {"class":"Grid__cell flx-s:1 p-r:4"})
    title = page_soup.find("meta", {"itemprop":"name"})["content"]
    aux = ''
    aux2 = ''
    for body in bodys:
        aux = aux + body.p.text
    aux2 = aux.replace('\t', '')
    aux2 = aux2.replace('\n\n', '\t')
    aux2 = aux2.replace('\n', ' ')
    aux2 = aux2.replace('  ', ' ')
    aux2 = aux2.replace('\t', '\\n\\n')
    aux2 = aux2.replace('"', '\\"')
    f =  open ('Ted Body' + '_' + str(my_urls.index(i)) + '.json', 'w',encoding="utf8")
    f.write('{\n\t"title": "'+title+'",\n\t"author": "'+author+'",\n\t"body": "'+aux2+'",\n\t"type": "video",\n\t"url": "'+i+'"\n}')
    f.close()


    
    
