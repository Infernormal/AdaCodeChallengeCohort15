# !/bin/python3


def subscription_summary(months_subscribed, ad_free_months, video_on_demand_purchases):
    """
    Parameters:
      months_subscribed: How many months each account purchased.
      ad_free_months: How many months each account paid for ad free viewing.
      video_on_demand_purchases: How many Videos on Demand each account purchased.
    """
    # Price for each service
    one_month_price = 7.00
    bundle = 18.00
    add_free = 2.00
    video_on_demand = 27.99

    accounts_count = len(months_subscribed)

    # Updating Each list with calculation of cost for each Account
    # Ad free total
    for i in range(accounts_count):
        ad_free_months[i] *= add_free

    # Video on demand total
    for i in range(accounts_count):
        video_on_demand_purchases[i] *= video_on_demand

    # Months subscribed total
    # Handeling the special case for 3 months bundle (3,6,9 etc.)
    for i in range(accounts_count):
        a = months_subscribed[i] // 3
        b = months_subscribed[i] % 3
        months_subscribed[i] = a * bundle + b * one_month_price

    # Creating the list for total earnings of each account
    total_account = []
    for i in range(accounts_count):
        total_sum = months_subscribed[i] + ad_free_months[i] + video_on_demand_purchases[i]
        total_account.append(total_sum)

    # Calculating the index of the account that earned the most, we will need it later
    index_max = 0
    for i in range(accounts_count):
        if total_account[index_max] < total_account[i]:
            index_max = i

    # Printing out the Output using string interpolation
    print("Welcome to the Ada+ Account Dashboard\n")
    for i in range(accounts_count):
        print(f"Account {1 + i} made ${round(total_account[i], 2)} total")
        print(f">>> ${months_subscribed[i]} from monthly sibscription fees")
        print(f">>> ${ad_free_months[i]} from Ad-free upgrades")
        print(f">>> ${round(video_on_demand_purchases[i], 2)} from Video on Demand purchases\n")
    print(f"Combined all accounts made ${round(sum(total_account), 2)} total")
    print(
        f"Premium content (Ad-free watching and Video on Demand) made ${round(sum(video_on_demand_purchases) + sum(ad_free_months), 2)} total\n")

    print(f"${round(max(total_account), 2)} was the most earned by any single account")
    print(f"The accounts that earned the most were: #{index_max + 1}")


if __name__ == '__main__':