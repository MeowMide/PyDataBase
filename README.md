PyDataBase

PDB это Python библиотека которая нужна для создания базы данных. 

В базе данных можно хранить нужную вам информацию.
Работает она так: при создании базы данных создается специальная папка. Создавая ячейки создаются файлы в этой папке, а что либо записывая в ячейке это что либо записывается в файле.
Прошу не судить строго, это моя первая библиотека. Версия бета 0.1, 1 класс, 4 действия, 2 файла. Теперь к коду.

Для начала, нам надо импортировать саму библиотеку.

    Import PyDataBase

После этого идет работа с классом database. 

    Import PyDataBase as pdb

    db = pdb.database('DataBase name')

Мы установили в переменную то, с какой базой данной мы будем работать. Если этой базы данной не существует, то она будет создана автоматически.

Далее идет работа с действиями. Начнем с создания ячейки. Для этого нам понадобится newcell()

    Import PyDataBase as pdb

    db = pdb.database('DataBase name')
    db.newcell('Cell name', 'Text in cell')

В действии есть два параметра. Имя и текст, который будет записан в ячейку. Ну или же cellname и information

Переходим к новому действию. readcell(). Это действие которое прочитает ячейку.

    db.readcell('Cell name')

Тут уже есть только один параметр - название ячейки - cellname. 

Теперь мы переходим к последнему действию - writecell(), ну или же перезапись ячейки.

    db.writecell('Cell name', 'Text')

Здесь есть два параметра - имя ячейки и текст на перезапись(cellname и information).


Больше здесь нет контента, ибо это еще ранняя версия, но библиотека будет обновлятся.
    
