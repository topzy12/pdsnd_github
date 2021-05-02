import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
#this method is used for getting a valid city name from the user
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=['chicago','new york city','washington']
    try:
        while (city not in ['chicago','washington','new york city']):
            city=input('\nPlease enter a city name you wish to check for(chicago, new york city, or washington):\n').lower()
            if city not in ['chicago','new york city','washington']:
                print('\n You can only use a city from the list, please try again\n')
                continue
            else:
                break
    except Exception as e:
           print('Enter a valid city name:{}'.format(e))


    # get user input for month (all, january, february, ... , june)
    month=['all','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

    while (month not in ['all','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']):
        month=input('\nPlease enter a month you wish to check for(all,jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec\n):').lower()
        if month not in ['all','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']:
            print('\nYou can only use a month from the list, please try again\n')
            continue
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=['all','mon','tue','wed','thu','fri','sat','sun']

    while (day not in ['all','mon','tue','wed','thu','fri','sat','sun']):
        day=input('\nPlease enter a day you wish to check for(all,mon,tue,wed,thu,fri,sat,sun):\n').lower()
        if day not in ['all','mon','tue','wed','thu','fri','sat','sun']:
            print('\nYou can only use a day from the list, please try again\n')
            continue
        else:
            break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    most_common_month=df['Start Time'].dt.month.mode()[0]
    monthsArr = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
    month = monthsArr[most_common_month-1]
    print('\nThe most common month of travel is: {}\n'.format(month))

    # display the most common day of week
    most_common_day=df['Start Time'].dt.day.mode()[0]
    print('\nThe most common day of travel is: {}\n'.format(most_common_day))

    # display the most common start hour
    most_common_hour=df['Start Time'].dt.hour.mode()[0]
    if most_common_hour<12:
        print('\nThe most common hour of travel is: {} AM\n'.format(most_common_hour))

    elif most_common_hour>12 & most_common_hour<24:
        print('\nThe most common hour of travel is: {} PM\n'.format(most_common_hour-12))

    elif most_common_hour==24:
        print('\nThe most common hour of travel is: {} AM\n'.format(most_common_hour-12))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is: {}\n'.format(most_common_start_station))

    # display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print('\nThe most commonly used end station is: {}\n'.format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    freq_combine_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost frequent combination of start station and end station trip is {} and {}'.format(most_common_start_station,most_common_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('\nThe total travel time is: {}\n'.format(total_travel_time))

    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('\nThe mean travel time is: {}\n'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    usertype_count=df['User Type'].value_counts()
    print('\nCount of User types: {}\n'.format(usertype_count))

    # Display counts of gender
    if 'Gender' in df:
        gender_count=df['Gender'].value_counts()
        print('\nCount of Gender: {}\n'.format(gender_count))
    else:
        print('\nCount of Gender could not be displayed, the dataset does not contain information for Gender\n')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_dob=int(df['Birth Year'].min())
        print('\nEarliest Date of Birth: {}\n'.format(earliest_dob))
    else:
        print('\nEarliest Date of birth could not be determindd, the dataset does not contain information for Birth Year\n')

    if 'Birth Year' in df:
        most_recent_dob=int(df['Birth Year'].max())
        print('\nMost Recent Year of Birth: {}\n'.format(most_recent_dob))
    else:
        print('\nCannot display the most recent year of birth, the dataset does not contain information for Birth Year\n')

    if 'Birth Year' in df:
        Most_common_dob=int(df['Birth Year'].mode()[0])
        print('\nMost Common Year of birth: {}\n'.format(Most_common_dob))
    else:
        print('\nCannot display the most common year of birth, the dataset does not contain information for Birth Year\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data=input('\nWould you like to see first 5 rows of the raw data? Please enter yes or no:\n').lower()

        rows=5
        while True:
            if raw_data=='no':
                break

            print('First {} Rows:'.format(rows))
            result=df.head(rows)
            print(result)

            raw_data=input('\nWould you like to see 5 more rows of the raw data? Please enter yes or no:\n').lower()
            rows +=5


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
