from timeit import timeit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

from functools import wraps

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

# Speed up your query and filter big data with pandas code

food_name = ['pizza', 'ice-cream', 'egg-fire', 'vegetables', 'almond', 'arugala', 'artichoke',
             'applesauce', 'asian noodles', 'antelope', 'ahi tuna', 'albacore tuna', 'Apple juice',
             'Avocado roll', 'Bruscetta', 'bacon', 'black beans', 'bagels', 'baked beans', 'BBQ']



def get_data(size=1_000):
    df = pd.DataFrame()
    df['age'] = np.random.randint(18, 110, size)
    df['time_in_bed'] = np.random.randint(4, 12, size)
    df['pct_sleeping'] = np.random.rand(size)
    df['favourite_food'] = np.random.choice(food_name, size)
    df['hate_food'] = np.random.choice(food_name, size)
    return df


def reward_calculate(row):
    if row['age'] >= 90:
        return row['favourite_food']
    if row['time_in_bed'] > 5 and row['pct_sleeping'] > 0.5:
        return row['favourite_food']
    return row['hate_food']

'''
The problem
Reward calculate:
- if they were in bed for more then 5 hour and they were sleeping for more then 50% we give them their
  favorite food.
- otherwise we give them their hate food.
- if thry over 90 year old give their favorite food
'''


# Loop (Poor level)
@timeit
def loop_solve(df):
    for index, row in df.iterrows():
        df.loc[index, 'reward'] = reward_calculate(row)
    return df


# Apply (Average)
@timeit
def apply_solve(df):
    df['reward'] = df.apply(reward_calculate, axis=1)
    return df


# Vectorized (Best)
@timeit
def vectorized_solve(df):
    df['reward'] = df['hate_food']
    df.loc[((df['pct_sleeping'] > 0.5) & (df['time_in_bed'] > 5)) | (df['age'] > 90), 'reward'] = df['favourite_food']


if __name__ == '__main__':
    df = get_data(1000000)

    start_time = time.time()
    loop_solve(df)
    loop_time = time.time() - start_time

    start_time = time.time()
    apply_solve(df)
    apply_time = time.time() - start_time

    start_time = time.time()
    vectorized_solve(df)
    vectorized_time = time.time() - start_time

    #Plot data
    result = pd.DataFrame(
        [
            ["Loop", loop_time],
            ["Apply", apply_time],
            ["Vectorized", vectorized_time],
        ],
        columns=['Type', "Time"]
    )
    print('loop_time : ', loop_time)
    print('apply_time : ', apply_time)
    print('vectorized_time : ', vectorized_time)
    result.set_index('Type')['Time'].plot(kind='bar', title='Time to run reward in big data')
    plt.show()
