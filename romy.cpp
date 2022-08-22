#include<iostream>
using namespace std;

class Restaurant {
    private:
        string name;
        string address;
    public:
        Restaurant() = default;
        Restaurant(string name, string address) {
            this->name = name;
            this->address = address;
        };

        string getName() {
            return this->name;
        };

        string getAddress() {
            return this->address;
        };

        void setName(string address){
            this->address = address;
        };

        void setAddress(string address){
            this->address = address;
        };

};

class Menu {
    public:
        string name;
        Restaurant R;
        int price;
        int max_num_plates;
        int num_plate;

        Menu() = default;
        Menu(Restaurant R1, int price) {
            this->R = R1;
            this->price = price;
        };

        
        void addNumberOfPlates(int n){ this->num_plate++; };

        void add_or_reduce_price(int amount){
            //(3)
            this->price += amount;
        };
};

class Customer {
    public:
        string name;
        int expenditure;
        int num_plate;

        Customer() {
            expenditure = 0;
        }
        Customer(const Customer &any_customer) {
            expenditure = any_customer.expenditure;
        }
        void order(Menu m) {
            this->num_plate = m.num_plate;
            //verify
            // while (m.num_plate < m.max_num_plates)
            // {
            //     m.addNumberOfPlates(1);
            // }

            if (m.num_plate < m.max_num_plates) {
                ;
            }
            else {
                
            }
            
            //change exp
            expenditure += m.num_plate * m.price;
        }
};

int main() {
    Restaurant resto = Restaurant("Resto Kawasaki", "Bambili");
    Menu resto_menu = Menu(resto, 2000);
    resto_menu.name = "Fried Rice and Chicken";
    resto_menu.max_num_plates = 10;

    cout << "\n" << resto.getName() << "\n";
    cout << "\n" << resto_menu.name << "\n";
    
    //create array of n customer
    int n;
    cout << "\n Enter number of customers : ";
    cin >> n;
    Customer customers[100];

    for(int i = 0; i < n; i++){
        cout << "\nEnter customer "<<i + 1<<"'s name : ";
        cin >> customers[i].name;
        cout << "\nEnter number of plates : ";
        cin >> customers[i].num_plate;

        //utilize copy constructor
        // while (i > 0){
        //     customers[i+1] = customers[i];
        // }
        
    }


    //order a menu for each customer
    int length = sizeof(customers)/sizeof(customers[0]);
    for (int i = 0; i < length; i++) {
        customers[i].order(resto_menu);
    }

    //print customer who ordered
    cout << "\nCustomers who ordered : \n";
    for (int i = 0; i < length; i++) {
        if (customers[i].expenditure > 0) {
            cout << "\n" << customers[i].name << "\n";
        }
    }

    


    return 0;
}