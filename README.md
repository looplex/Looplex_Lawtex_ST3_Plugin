# Looplex Lawtex Plugin - Sublime Text 3

Este é o plugin da Looplex de suporte ao Lawtex e nossa plataforma para o [Sublime Text 3](https://www.sublimetext.com/3). Ele irá permitir a validação gramatical de arquivos Lawtex, assim como o upload de templates e anexos para a Looplex. 

## Instalação

Para o funcionamento do plugin, é necessário a instalação do [Java 8 JRE](https://www.oracle.com/br/java/technologies/javase-jre8-downloads.html). Após isso, basta incluir este repositório ao [Package Control do Sublime Text 3](https://packagecontrol.io/docs/usage). Para mais detalhes, siga o passo-a-passo a seguir:

##### Instalar o Java 8 JRE

- Visite https://www.oracle.com/br/java/technologies/javase-jre8-downloads.html 
- Encontre seu sistema operacional na lista de downloads e baixe a sua versão do Java 8 JRE.
- Após terminar o download, rode o executável para instalar o Java (ou extraia os arquivos e efetue sua configuração caso baixe o arquivo compactado).

##### Instalar o Package Control no Sublime Text 3

- Abra o Sublime Text 3
- Abra o menu _'Tools'_, e selecione _'Install Package Control...'_.
- Aguarde a instalação do Package Control ser concluída.
  - O progresso de instalação aparecerá na barra de status no lado inferior da janela do Sublime Text 3.

##### Adicionar o repositório do plugin ao Package Control

- Abra o menu _'Tools'_, e selecione _'Command Palette...'_
- Digite _'Package Control: Add Repository'_ e aperte Enter.
  - No canto inferior da janela aparecerá um campo de entrada.
- Copie e cole o endereço deste repositório (https://github.com/looplex/Looplex_Lawtex_ST3_Plugin) no campo de entrada que apareceu, e aperte Enter.

##### Instale o plugin

- Abra o menu _'Tools'_, e selecione _'Command Palette...'_
- Digite _'Package Control: Install Package'_ e aperte Enter.
  - Um novo menu irá aparecer depois de alguns segundos.
- Busque por _'Looplex_Lawtex_ST3_Plugin_, e aperte Enter.
- Aguarde a instalação do plugin ser concluída.
  - O progresso de instalação aparecerá na barra de status no lado inferior da janela do Sublime Text 3.


Caso necessite de ajuda, você pode entrar em contato com a Looplex.

## Utilização

### Validação de arquivo

Para validar um arquivo .lawtex, basta abrir o menu _'Looplex'_, e selecionar _'Validate File'_ (ou apertando _Ctrl+B_).

### Upload de templates

Para efetuar o upload de templates, abra o menu _'Looplex'_, e selecione _'Upload Template'_. O plugin irá validar a grámatica Lawtex do template, procurar por anexos e arquivos de estilo, e efetuar o upload destes para a plataforma da Looplex após seu login de usuário.

#### Inclusão de elementos de template de arquivos secundários

Para incluir um elemento de template de um arquivo secundário, basta incluir um comentário com o nome do elemento e o seu arquivo de origem. A seguir, alguns exemplos:

##### Inclusão de um elemento em um arquivo na mesma pasta

```
// import BRANCH_nome_de_branch from "nome_do_arquivo"
```

##### Inclusão de múltiplos elementos em um arquivo na mesma pasta

```
// import [BRANCH_nome_de_branch_1, BRANCH_nome_de_branch_2, BRANCH_nome_de_branch_3] from "nome_do_arquivo"
```

##### Inclusão de elementos em um arquivo em uma subpasta

```
// import BRANCH_nome_de_branch from "subpasta/nome_do_arquivo"
// import [BRANCH_nome_de_branch_1, BRANCH_nome_de_branch_2] from "subpasta/outra_subpasta/nome_do_arquivo"
```

##### Inclusão de elementos em um arquivo em pastas acimas

- Uma pasta acima
```
// import BRANCH_nome_de_branch from "../nome_do_arquivo"
```
- Duas pastas acima
```
// import BRANCH_nome_de_branch from "../../nome_do_arquivo"
```
- Três pastas acima
```
// import [BRANCH_nome_de_branch_1, BRANCH_nome_de_branch_2] from "../../../nome_do_arquivo"
```

#### Exclusão de elementos de template

Para a exclusão de um elemento de template (que não se encontra localmente, mas contém uma versão na nuvem), basta incluir um comentário com o elemento a ser excluído da verificação de upload. Esses anexos devem estar na mesma pasta que o arquivo .lawtex que os utilizam. A seguir, alguns exemplos:

##### Exclusão de um elemento

```
// ignore BRANCH_nome_de_branch
```

##### Exclusão de múltiplos elementos

```
// ignore [BRANCH_nome_de_branch_1, BRANCH_nome_de_branch_2]
```

#### Inclusão de anexos

Para a inclusão de arquivos de anexo (como imagens, exemplo), basta incluir um comentário com o elemento a ser adicionado. A seguir, alguns exemplos:

##### Inclusão de um anexo

```
// attach "arquivo_anexo.png"
```

##### Inclusão de múltiplos anexos

```
// attach ["arquivo_anexo_1.png", "arquivo_anexo_2.png", "arquivo_anexo.png"]
```
