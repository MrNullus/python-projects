"""
    @ Erros sempre vão ocoorer porra lembre-se disso! @
        $> Linguagens modernas como Python, usam tratamentos de erros e exceções
        $> Existem varios tipos de erros, alguns são:>>
            $>> Erros de sintaxes - são erros que acontecem quando a sintaxe é escrita de forma errada
            $>> Erros de semantica - erros que acontecem quando  o sentido é feito errado (meio vago pra karai né, irmão? Mas fica relex depois que pratica entende direitinho)
"""

# $> Se liga ai, esse é um erro de sintaxe
# $> Pois o primt está escrito errado mané
#primt("Hello Porra! Fica atendo aos erros mano karai")

# $> Presta atenção corno, isso aqui é um erro de semantica
# $> Sabe porque? Simples, mané. A variavel seFudeu não está definida então vai dar erro de semantica brô
# ! prestenção esse é um errro de semantica classificado como -> NameError ( Erro de Nome) !
#print(seFudeu)

"""
    ERROS EM PYTHON SÃO VISTOS COMO EXCEÇÕES ( OU PELO MENOS FAZEM UMA ANALOGIA A EXCESSÃO )
        # Algumas exceções:>
            $> NameError - Erro de nome ( provavelmente seu ze ruela tu teve erro nas variaveis, então confere elas)
            $> TypeError - Erro de tipo ( erros de tipos, ou seja, tipos de variaveis ou algo do tipo está errado )
            $> IndexError - Erro de Indexação ( são erros de indexs, causados por algum indice errado mano )
            $> ZeroDivisonError - Erro de divisão Por Zero - ( erro causado por que não se pode dividir opor zero ou seja o denominador não pode ser zero )
            $> ModuleNotFounderError - Erro de Modulo Não encontrado ( se dá esse erro, por causa de modulo não encontrado )
        ! Tem mais exceções que isso, funciona no Python como uma grande árvore, para conferir isso proucure no google seu merda isso aqui:>>  !
        !    *    Python exceptions errors     *    ! 
    
    +     Try - Except       +
        $> Essa é uma estrutura usada para tratamento de erros e exceções
        $> Sintaxe:>>
            try: 
                operação para tentar fazer
            except: 
                operação caso der erro, ou seja caso ocorra a exceção
        
        $> else / finally parametros opcionais
            $>> Sintaxe:>>
               try: 
                    operação para tentar fazer
                except:
                    operação caso de error, ou seja felas da puta caso ocorra uma exceção
                else: 
                    operação caso de sucesso
                finally: 
                    essa operação vai ocorrer mesmo que caso de erro ou acerto        
"""

try:
    a = int(input('Numerador:>>   '))
    b = int(input('Denominador:>> '))
    r = a/b
                     # esssa variavel vai receber o erro
except Exception as erro:
    print(f'+- Deu erro, {erro.__class__}') # "erro.__class__" Vai capturar a classe do erro
else:
    print(f'O resultado foi : {r:.1f}')
finally:
    print('Volte sempre rapa! Muito obrigado valeu irmão')

