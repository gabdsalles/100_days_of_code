import pandas as pd

esquilos_df = pd.read_csv('./Day 25 - CSV/squirrel_count.csv')
esquilos_gray = esquilos_df['Primary Fur Color'][esquilos_df['Primary Fur Color'] == 'Gray'].count()
esquilos_cinnamon = esquilos_df['Primary Fur Color'][esquilos_df['Primary Fur Color'] == 'Cinnamon'].count()
esquilos_black = esquilos_df['Primary Fur Color'][esquilos_df['Primary Fur Color'] == 'Black'].count()

data_dict = {
    'color': ['Gray', 'Cinnamon', 'Black'],
    'quantity': [esquilos_gray, esquilos_cinnamon, esquilos_black]
}

new_df = pd.DataFrame(data_dict)
new_df.to_csv('./Day 25 - CSV/cont_esquilos.csv')


