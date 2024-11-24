import json

def json_gen(words, datafilename):
    
    f = open(datafilename, "w")
    f.write('[\n')

    word_count = 1
    
    for word in words:

        json_word = '{\n'

        word_sylls = word.split(',')
        word_full = word.replace(",", "")

        while len(word_sylls) < 5:
            word_sylls.append("")
        
        json_word += '"word":"' + word_full + '",\n'

        syll_count = 1
        for syll in word_sylls:
            json_word += '"syllable' + str(syll_count) + '":"'  + syll + '",\n'
            syll_count += 1

        json_word += '"RECORD": "<button type=\\"button\\" class=\\"btn btn-danger\\" id=\\"rec_stop_{0}\\" onclick=\\"myFunction({0})\\"><span style=\\"font-size:25px;\\">REC</span></button>",\n'.format(str(word_count))
        json_word += '"PLAY": "<div class=\\"audio' + str(word_count) + '\\" id=\\"audio' + str(word_count) + '\\"></div>"\n},\n'

        word_count += 1

        f.write(json_word)
    
    f.write('\n]')

th_words = ["thumb", "thin", "think", "ther,mom,et,er",
    "thir,ty", "thir,teen", "thun,der", "thick", "thir,sty",
    "thigh", "thank, you", "ther,a,py, dog", "smoo,thie", "bath,tub",
    "ba,thing", "fea,ther", "to,ge,ther", "bath,room", "weal,thy",
    "heal,thy", "mo,ther", "fa,ther", "birth,day", "wea,ther", "moth",
    "bath", "teeth", "path", "tooth", "earth", "math", "booth", "month",
    "mouth", "breath", "wealth", "thumb", "month", "think", "feather",
    "earth", "thir,ty", "smoo,thie", "thick", "mo,ther", "mouth", "birth,day",
    "teeth"]

three_syll_words = ["chew,ing, gum", "fing,er,nail", "kan,ga,roo", "il,le,gal", "ma,ga,zine","mar,i,gold","re,gu,lar", "spa,ghet,ti", "Thanks,giv,ing", "care,ful,ly", "wa,ter,fall", "au,to,graph", "um,bre,lla",
                        "dif,fi,cult", "fac,to,ry", "fam,i,ly", "fing,er,print", "fur,ni,ture", "phy,si,cian", "sand,pa,per", "won,der,ful", "thun,der,storm", "chick,en,pox", "syl,la,ble", "por,ta,ble",
                        "Oc,to,ber", "cu,cum,ber", "sil,ver,ware", "ra,di,o", "re,a,rrange", "rel,a,tive", "ru,bber,band", "an,y,place", "re,com,mend", "na,tur,al", "nur,se,ry", "nee,dle,point", "a,ccom,plish", "Ken,tuck,y", "yes,ter,day",
                        "for,get,ful", "Sep,tem,ber", "de,part,ment", "car,pen,ter", "pro,pell,er", "te,le,phone", "Sa,tur,day", "va,ni,shing", "ca,mer,a ", "De,cem,ber", "fi,ni,shing", "la,dy,bug", "o,ver,board", "gra,vi,ty", "ham,bur,ger",
                        "gar,de,ner", "mul,ti,ply", "re,por,ter", "vi,ta,min","fa,mi,ly", "e,le,phant", "en,ve,lope", "a,cro,bat", "cu,sto,mer", "fe,ver,ish", "ho,li,day", "af,ter,noon", "fan,ta,stic", "mi,ni,ster", "un,der,stand", "re,comm,end",
                        "happ,en,ing", "le,mo,nade", "bal,co,ny", "e,ner,gy", "jell,y,fish", "app,e,tite", "va,len,tine", "en,ter,tain", "li,ber,ty", "lott,er,y", "pro,per,ty", "ten,den,cy", "an,ce,stor", "di,sa,ster", "re,gi,ster", "me,di,cine",
                        "sen,si,tive", "ve,ni,son", "me,di,um", "ra,di,o", "mu,si,cal", "hi,ber,nate", "char,ac,ter", "ga,so,line"]

four_syll_words = ["com,pan,ion,ship", "un,im,por,tant", "ac,ci,den,tal", "fun,da,men,tal", "le,gis,la,tion", "am,pli,fi,er", "ex,plor,a,tion", "un,em,ploy,ment", "a,ddi,tion,al", "e,mo,tion,al", "ac,cep,ta,ble",
                    "con,ver,ti,ble", "de,pen,da,ble", "ques,tion,a,ble", "life, pre,ser,ver", "li,bra,ri,an", "lo,co,mo,tive", "a,rith,me,tic", "ma,ga,zine, rack", "Co,lo,ra,do", "kin,der,gar,ten", "com,bi,na,tion",
                    "co,in,ci,dence", "con,gra,tu,late", "e,mer,gen,cy", "neu,ro,lo,gy", "gen,er,a,tion", "har,mon,i,ca", "hel,i,cop,ter", "a,gri,cul,ture", "ge,o,gra,phy", "co,ffee, grin,der", "dis,or,ga,nized",
                    "for,gett,a,ble", "gra,du,a,tion", "grand,fa,ther, clock", "al,li,ga,tor", "sig,ni,fi,cant", "in,fre,quent,ly", "re,frig,er,ate"]

json_gen(th_words,"data_th.json")
json_gen(three_syll_words,"data_3_syll.json")
json_gen(four_syll_words,"data_4_syll.json")