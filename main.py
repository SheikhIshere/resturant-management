from Order import Order
from restaurent import Restaurant
from menu import Pizza, Burger, Drinks, Menu
from user import Chef, Server, Manager, Customer

def main():
    menu = Menu()
    pizza_1 = Pizza('Shutki Pizza', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('alur vorta pizza', 400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('dal pizza', 500, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    # adding burger to the menu
    burger_1 = Burger('naga burger', 1000, 'chicken', ['bread', 'chilli'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('beef burger', 500, 'beef', ['bread', 'chilli'])
    menu.add_menu_item('burger', burger_2)

    # adding drinks to the menu
    coke = Drinks('coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Mocha', 300, False)
    menu.add_menu_item('drinks', coffee)
    
    # show menu
    # menu.show_menu()

    restaurant = Restaurant('sai baba restaurant',10000, menu)

    # add employees
    manager = Manager('kala chan manager', 5, 'kalachan@gmail.com', 'kalipur', 1500, 'jan 1 2020', 'core')
    restaurant.add_employee('manager', manager)
    chef = Chef('rustom baburchi', 6, 'chupa@rustom.com', 'rustomnagar', 3500, 'feb 1, 2020', 'Chef', 'everything')    
    restaurant.add_employee('chef', chef)
    server = Server('chotu server', 6, 'nai@jai.com', 'kalipur', 200, 'march 1, 2020', 'server')
    restaurant.add_employee('server', server)

    # showing employees
    # restaurant.show_employees() #why it's not showing up
    #kjfdhjghkj

    # customer 
    customer_1 = Customer('sakib khan', 6, 'king@khan.com', "banani", 100000)
    order_1 = Order(customer_1, [pizza_3,burger_1, burger_2, coffee, coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    # customer one paying for order 1
    restaurant.receive_payment(order_1,200000, customer_1)

    print('revenue and balance after first customer ', restaurant.revenue, restaurant.balance)

    # customer 2
    customer_2 = Customer('sakib al hasan', 6, 'king@khan.com', "banani", 100000)
    order_2 = Order(customer_2, [pizza_1,pizza_2, burger_2, coffee, burger_1])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)
    restaurant.receive_payment(order_2, 500000, customer_2)
    print('revenue and balance after second customer ', restaurant.revenue, restaurant.balance)

    # pay rent
    print('before rent ', restaurant.revenue, restaurant.balance, restaurant.expense)
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('after rent ', restaurant.revenue, restaurant.balance, restaurant.expense)

    restaurant.pay_salary(chef)
    print('after pay chef ', restaurant.revenue, restaurant.balance, restaurant.expense)


if __name__ == '__main__':
    main()