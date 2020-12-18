import pandas as pd
import seaborn as sns

# -- 오류시
# pip uninstall matplotlib
# pip install matplotlib==3.2
# pip install numpy==1.19.3

# tips = sns.load_dataset('tips')
# print(tips)
movies = pd.read_csv('data/movie.csv')
print(movies)