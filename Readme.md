# NumPy tutorial

NumPy (Numerical Python) - бібліотека для роботи з масивами, має ф-ї для лінійної алгебри, перетворення Фур'є та матриць. Надає об'єкт масиву, набагато швидший за стандартні списки.

## Підручник NumPy

**Встановлення та імпорт**  
`$ pip install numpy` встановити для поточного оточення  
`import numpy`, `import numpy as np` підключити до робочого файлу  
`print(np.__version__)` повертає версію  

**Створення масивів**  
`arr = np.array([1, 2, 3])` створити масив на основі списку; приймає будь-який контейнерний тип; аргумент `ndim=n` задає кількість вимірів  

**Доступ до елементів, зрізи**  
Індексація, негативна індексація, зрізи одновимірних масивів відповідно до загальних правил контейнерних типів  
`arr[1, 2]` повертає 3 елемент 2 рядка двомірного масиву  
`arr[1:3, 2:5]` повертає матрицю зрізів [2:5] рядрів [1:3]

**Типи даних**  
`i` ціле, `b` логічне, `u` ціле без знаку, `f` дробове,  
`c` комплексне дробове, `m` дельта часу, `M` дата/час,  
`O` об'єкт, `S` рядок, `U` рядок Unicode,  
`V` фіксований шматок пам'яті для інших типів (void)  
`arr.dtype` поаертає тип даних масива  
`np.array([1, 2, 3], dtype='S')` задає тип даних  
для `i`, `u`, `f`, `S`, `U` можна визначити розмір (i4 - 4 байти)  
за неможливості перетворити тип видає ValueError  
`arr.astype('i')`, `arr.astype(int)` поверне масив перетворених  

**Копія та перегляд**  
Копія володіє власними даними, перегляд - ні.  
`arr.copy()` повертає копію масива, зміни не розповсюджуються  
`arr.view()` повертає новий вигляд масиву з тими ж даними;  
зміна даних у вихідноому масиві або представленнях змінюють всюди  
`arr.base()` повертає None, якщо масив володіє власними даними  
або вихідний масив, якщо власними даними не володіє

**Форма масиву**  
Форма масиву - кількість елементів в кожному вимірі  
`arr.shape` повертає форму ((2, 3) для [[1, 2, 3], [4, 5, 6]])  
`arr.reshape(3, 2)` повертає масив відповідно до форми;  
форма може бути змінена лише відповідно до кількості елементів;  
reshape повертає представлення (зміна елемента);  
останній вимір може бути визначено автоматично reshape(2, -1)  

**Ітерації**  
Ітерації проходять відповідно до стандартного ітерування python  
`for item in arr:` ітерується по першому рівню вкладеності;  
вкладені цикли дають змогу ітерувати глибше  
`for item in np.nditer(arr)` надає глибоке ітерування;  
для зміни типу додатково `flags=['buffered'], op_dtypes=['S']`  
`for item in np.nditer(arr[:, ::2])` діапазон за правилами зрізів  
`for i, x in np.ndenumerate(arr):` надає кортеж індексів  

**Об'єднання масивів**  
`np.concatenate()` повертає об'єднання масивів;  
перший аргумент примає кортеж насивів, які необхідно об'єднати;  
другий (необов.) аргумент - вісь, за якою об'єднати (за ум.: 0)  
`np.stack()` повертає об'єднання масивів вздовж нової осі  
`np.hstack()` - укладання в стек вздовж рядків  
`np.vstack()` - укладання в стек вздовж стовпців  
`np.dstack()` - укладання в стек по виситі, що дорівнює глибині  

**Розбиття масивів**