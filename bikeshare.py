import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities=['chicago','new york city','washington']
        months=['all','january','february','march','april','may','june']
        days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        try:
            city = str(input('Would you like to see data for Chicago, New York City, or Washington?'))
            if city.lower() == "washington":
                print('\nGender and Birth Year datas are not available.\n')
                new_city=input('\nAre you sure you want to choose Washington? Enter yes or no.\n')
                if new_city.lower() != "yes":
                    raise ValueError ('Please enter another city name.\n')

            if city.lower() not in cities:
                raise ValueError ('Unvalid city! Please try again :) \n')

    # TO DO: get user input for month (all, january, february, ... , june)
            month = str(input('Which month - All, January, February, March, April, May, or June?\n'))
            if month.lower() not in months:
                raise ValueError ('Unvalid month! Please try again :) \n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = str(input('Which day - All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n'))
            if day.lower() not in days:
                raise ValueError ('Unvalid day! Please try again :) \n')

            break

        except ValueError as ve:
            print(ve)

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month']==month]
    elif month == 'all':
        df = df
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    elif day == 'all':
        df = df

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # find the most popular month
    popular_month = df['month'].mode()[0]
    print("The most popular month is {}.\n".format(popular_month))

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract day from the Start Time column to create an hour column
    df['day'] = df['Start Time'].dt.weekday_name

    # find the most popular day
    popular_day = df['day'].mode()[0]
    print("The most popular day is {}.\n".format(popular_day))

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular start hour is {}.\n".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip']="from " + df['Start Station'] + " to " + df ['End Station']
    popular_trip = df['Trip'].mode()[0]
    popular_trip_count=df['Trip'].value_counts()[0]

    print("Most popular start station: {}.".format(popular_start_station))
    print("Most popular end station: {}.".format(popular_end_station))
    print("Most popular trip: {} and it was done {} time(s).".format(popular_trip,popular_trip_count))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration

    Args:
        df - Pandas DataFrame containing city data filtered by month and day

    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    hour_tot=total_travel_time/3600
    minute_tot=(total_travel_time%3600)/60
    second_tot=(total_travel_time%3600)%60
    print("The total travel time is {} hour(s) {} minute(s) and {} second(s).".format(int(hour_tot),int(minute_tot),int(second_tot)))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    hour_mean=mean_travel_time/3600
    minute_mean=(mean_travel_time%3600)/60
    second_mean=(mean_travel_time%3600)%60
    print("The mean travel time is {} hour(s) {} minute(s) and {} second(s).".format(int(hour_mean), int(minute_mean),int(second_mean)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city,current_year):
    """Displays statistics on bikeshare users.

     Args:
         df - Pandas DataFrame containing city data filtered by month and day
        (str) city - name of the city to analyze
        (int) current_year - current year to calculate customer age

    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types breakdown:\n {}.\n".format(user_types))

    # TO DO: Display counts of gender / Not available for Washington
    if city.lower() != 'washington':
        gender_count = df['Gender'].value_counts()
        print("Gender counts:\n {}.\n".format(gender_count))

        # TO DO: Display earliest, most recent, and most common year of birth
        year_min=df['Birth Year'].max()
        year_max=df['Birth Year'].min()
        year_common=df['Birth Year'].mode()[0]
        print("The youngest customer was born in year {}.".format(int(year_min)))
        print("The oldest customer was born in year {}.".format(int(year_max)))
        print("The most common year of birth is {}.".format(int(year_common)))

        #Display mean user age
        year_mean=df['Birth Year'].mean()
        print("The mean users age is {}.".format(current_year-int(year_mean)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df,city,nbr_lines):
    """ prompt the user to see 5 lines of raw data, continue these prompts and displays until the user says 'no'
     Args:
         df - Pandas DataFrame containing city data filtered by month and day
        (str) city - name of the city to analyze
        (int) lines - number of lines that the user wants to display

    """
    start=0
    more_data = 'yes'
    while more_data == 'yes':
        for i in range(start*nbr_lines,(start+1)*nbr_lines):
            print (" Start time: {} \n End time: {}\n Trip Duration(second): {} \n Start Station:{} \n End Station: {}" \
            .format(df.values[i,1],df.values[i,2], df.values[i,3], df.values[i,4],df.values[i,5]))
            if city.lower()=='washington':
                print (" User type: {} \n ".format(df.values[i,6]))
            else:
                print (" User type: {} \n Gender: {} \n Birth Year: {} \n".format(df.values[i,6], df.values[i,7],df.values[i,8]))
        more_data = input('\n Do you want to see {} lines more ? Enter yes or no.\n'.format(int(nbr_lines)))
        start+=1



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city,2018)
        # Ask the user if raw data should be displayed
        raw_data = input('\nDo you want to see 5 lines of raw data? Enter yes or no.\n')
        if raw_data.lower() == 'yes':
            display_data(df,city,5)

        # Restart the program
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
