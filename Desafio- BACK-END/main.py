#Fazendo o import do FastAPI para criação da api e da HTTPException para retorno de erro.
from fastapi import FastAPI, HTTPException
#Realizando o import da biblioteca pydantic para a construção do BaseModel.
from pydantic import BaseModel
#Fazendo o import da biblioteca pandas para a manipulação dos dados.
import pandas as pd

#Declarando a criação da api.
app = FastAPI()

#Criando e tipando o BaseModel
class ProductCreate(BaseModel):
    nome: str
    numero_do_produto: str
    cor: str
    preco_padrao: float

#Função para a criação de novos produtos.
@app.post("/products/")
def create_product(product: ProductCreate):
    data = pd.read_csv('AdventureWorks_Products.csv')  
    new_product = {
        'nome': product.nome,
        'numero_do_produto': product.numero_do_produto,
        'cor': product.cor,
        'preco_padrao': product.preco_padrao
    }
    data = data.append(new_product, ignore_index=True)
    data.to_csv('AdventureWorks_Products.csv', index=False)
    return {"message": "Product created successfully"}

#Função para consultar todos os produtos.
@app.get("/products/")
def read_all_products():
    data = pd.read_csv('AdventureWorks_Products.csv')
    return data.to_dict(orient='records')

#Função para consultar os produtos especificado pela numerção = id.
@app.get("/products/{id}")
def read_product(id: int):
    data = pd.read_csv('AdventureWorks_Products.csv')
    product = data[data['id'] == id]
    if len(product) == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return product.to_dict(orient='records')[0]

#Função para modificar produto pela numeração = id.
@app.put("/products/{id}")
def update_product(id: int, product: ProductCreate):
    data = pd.read_csv('AdventureWorks_Products.csv')
    updated_product = {
        'nome': product.nome,
        'numero_do_produto': product.numero_do_produto,
        'cor': product.cor,
        'preco_padrao': product.preco_padrao
    }
    data.loc[data['id'] == id] = updated_product
    data.to_csv('AdventureWorks_Products.csv', index=False)
    return {"message": "Product updated successfully"}

#Função para deletar produto pela numeração = id.
@app.delete("/products/{id}")
def delete_product(id: int):
    data = pd.read_csv('AdventureWorks_Products.csv')
    data = data[data['id'] != id]
    data.to_csv('AdventureWorks_Products.csv', index=False)
    return {"message": "Product deleted successfully"}

#Rota 1: que retorna os 10 produtos mais vendidos na categoria fornecida.

@app.get("/sales/top-products/category/{category}")
def get_top_products_by_category(category: str):
    products = pd.read_csv('AdventureWorks_Products.csv')  
    sales_2015 = pd.read_csv('AdventureWorks_Sales_2015.csv')
    sales_2016 = pd.read_csv('AdventureWorks_Sales_2016.csv')
    sales_2017 = pd.read_csv('AdventureWorks_Sales_2017.csv')

    # Concatena as vendas de todos os anos
    sales = pd.concat([sales_2015, sales_2016, sales_2017])

    # Retorna os detalhes dos produtos
    return

#Rota 2: que retorna o cliente com o maior número de pedidos realizados.
@app.get("/sales/best-customer")
def get_best_customer():
    customers = pd.read_csv('AdventureWorks_Customers.csv')  
    sales_2015 = pd.read_csv('AdventureWorks_Sales_2015.csv')
    sales_2016 = pd.read_csv('AdventureWorks_Sales_2016.csv')
    sales_2017 = pd.read_csv('AdventureWorks_Sales_2017.csv')

    # Concatena as vendas de todos os anos
    sales = pd.concat([sales_2015, sales_2016, sales_2017])

   
    return

#Rota 3: que retorna o mês com mais vendas (em valor total).

@app.get("/sales/busiest-month")
def get_busiest_month():
    sales_2015 = pd.read_csv('AdventureWorks_Sales_2015.csv')
    sales_2016 = pd.read_csv('AdventureWorks_Sales_2016.csv')
    sales_2017 = pd.read_csv('AdventureWorks_Sales_2017.csv')

    # Concatena as vendas de todos os anos
    sales = pd.concat([sales_2015, sales_2016, sales_2017])


    # Retorna o mês e o ano
    return 


#Rota 4: que retorna os vendedores que tiveram vendas com valor acima da média no último ano fiscal.

@app.get("/sales/top-sellers")
def get_top_sellers():
    sellers = pd.read_csv('AdventureWorks_Territories.csv')  # Como não tinha lista de vendedores, estou partindo para os territórios que mais venderam.
    sales_2015 = pd.read_csv('AdventureWorks_Sales_2015.csv')
    sales_2016 = pd.read_csv('AdventureWorks_Sales_2016.csv')
    sales_2017 = pd.read_csv('AdventureWorks_Sales_2017.csv')

    # Concatena as vendas de todos os anos
    sales = pd.concat([sales_2015, sales_2016, sales_2017])

    return

# Para executar o código é necessário:
# Certifique-se de ter todas as dependências instaladas. Para instalar são necessários os seguintes passos:
# 'pip install fastapi pandas uvicorn'
# 'main\Scripts\activate'

# Para iniciar o servidor FastAPI e executar o código, use o seguinte comando no terminal:
# 'uvicorn main:app --reload'
# Isso iniciará o servidor FastAPI e permitirá que você acesse a API em http://localhost:8000. 
# O parâmetro --reload permite que o servidor seja reiniciado automaticamente sempre que houver alterações no código.