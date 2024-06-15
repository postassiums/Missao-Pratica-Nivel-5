from faker import Faker
faker = Faker('pt_BR')

dados=[]

for i in range(10):
  dados.append({"name": faker.name(),"points":faker.random_int(min=1,max=100)})


import json

with open('alunos.txt','w') as f:
  json.dump(dados,f)
  
  

dados=[]
with open('alunos.txt','r') as f:
  dados = json.load(f)







from wordcloud import WordCloud

nomes =''
for dado in dados:
  nomes+=f"{dado['name']},"

nomes=nomes[:-1]


nuvem_palavras = WordCloud(background_color='grey',
                           width=800,height=400).generate(nomes)
plt.imshow(nuvem_palavras, interpolation='bilinear')
plt.axis("off")
nuvem_palavras.to_file("Nuvem de palavras.png")

