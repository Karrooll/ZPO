#include <cmath>
#include <iostream>
#include "package.hpp"
#include "types.hpp"
#include "storage_types.hpp"
#include "helpers.hpp"
#include "nodes.hpp"
#include <map>
#include <sstream>

void print(std::vector<ElementID> a) {
    for (unsigned int i : a)
        std::cout<<i<<" ";
    std::cout<<std::endl;
}
void bufferstatus (Ramp& rampa,std::string message=""){
    bool a = rampa.get_sending_buffer().has_value();
    if (a)
        std::cout<<"BUFOR JEST PELNY!"<<message<<std::endl;
    else
        std::cout<<"BUFOR JEST PUSTY!"<<message<<std::endl;
}
void bufferstatus (Worker& robol,std::string message=""){
    bool a = robol.get_sending_buffer().has_value();
    if (a)
        std::cout<<"BUFOR JEST PELNY!"<<message<<std::endl;
    else
        std::cout<<"BUFOR JEST PUSTY!"<<message<<std::endl;
}

int main() {
    std::cout << "Welcome in spiulkolot! =^.^=" << std::endl;
     ReceiverPreferences rp;
    Storehouse magazyn1 = Storehouse(1);
    Storehouse magazyn2 = Storehouse(2);
    Storehouse magazyn3 = Storehouse(3);
    rp.add_receiver(&magazyn1);
    rp.add_receiver(&magazyn2);
    rp.add_receiver(&magazyn2); //sprawdzenie czy dodanie jeszcze raz istniejacego nie rozwali prawdopodobienstw
    rp.add_receiver(&magazyn3);
    auto it = rp.begin();
    it++;
    it++;
    std::cout<<it->second<<std::endl;
    Ramp r(1,2);
    auto recv = std::make_unique<Storehouse>(1);
    r.receiver_preferences_.add_receiver(recv.get());
    r.deliver_goods(1);
    r.send_package();
    r.deliver_goods(2);
    r.deliver_goods(3);
    r.send_package();
    r.deliver_goods(4);
    r.deliver_goods(5);
    r.send_package();
    bufferstatus(r," (Test Rampy - czy pojawil sie produkt w buforze)");
    Worker w(1, 2, std::make_unique<PackageQueue>(PackageQueueType::FIFO));
    Storehouse magazyn5 = Storehouse(5);
    w.receiver_preferences_.add_receiver(&magazyn5);
    w.receive_package(Package(4)); //UWAGA NA ZAJETE WCZESNIEJ ID!!! JESLI JEST ZAJETE BEDZIE 0
    w.do_work(1);
    w.receive_package(Package(5));
    w.receive_package(Package(6));
    w.receive_package(Package(7));
    w.do_work(2);
    w.do_work(3);
    w.do_work(4);
    w.do_work(5);
    w.do_work(6);
    //w.do_work(7);

    bufferstatus(w," (Test Workera - czy ma produkt na rece (w buforze))");
    auto& buffer = w.get_sending_buffer();
    if(buffer.has_value())
        std::cout<<"ID produktu z bufora "<<buffer.value().get_id()<<std::endl;
    return 0;
}
