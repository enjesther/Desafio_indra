#language:pt
Funcionalidade: ir no menu dia das mães e selecionar uma categoria e apresentar um produto
    Cenario: apresentar um produto a partir do menu dia das maes
        Dado que esteja na tela inicial da americanas
        Quando selecionado o menu dia das mães
        E selecionar a categoria Moda
        E selecionar a categoria moda praia
        E selecionar o produto
        Então deve ser apresentado a pagina do produto