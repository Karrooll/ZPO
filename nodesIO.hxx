#ifndef NETSIM_NODES_HPP
#define NETSIM_NODES_HPP

#include <map>
#include <memory>
#include <utility>
#include "storage_types.hxx"
#include "types.hxx"
#include "helpers.hxx"

enum class ReceiverType{
    WORKER,
    STOREHOUSE
};

class IPackageReceiver{
public:
    using const_iterator = IPackageStockpile::const_iterator;
    virtual void receive_package(Package&& p)=0;
    ElementID get_id() const {return id_;};
    ReceiverType get_receiver_type() const {return rt_;};
    virtual ~IPackageReceiver() = default;
protected:
    ElementID id_;
    ReceiverType rt_;
};

class Storehouse : public IPackageReceiver{
public:
    const_iterator begin() const { return d_->begin(); }
    const_iterator end() const { return d_->end(); }
    const_iterator cbegin() const { return d_->begin(); }
    const_iterator cend() const { return d_->end(); }
    explicit Storehouse(ElementID id, std::unique_ptr<IPackageStockpile> d = std::make_unique<PackageQueue>(PackageQueueType::FIFO));
    void receive_package(Package &&p) override {d_->push(std::move(p));};
    bool operator <(const Storehouse& obj) const {return id_ < obj.get_id();};
private:
    std::unique_ptr<IPackageStockpile> d_;
};

class ReceiverPreferences{
public:
    using preferences_t = std::map<IPackageReceiver*, double>;
    using const_iterator = preferences_t::const_iterator;
    const_iterator begin() const { return preferences_.begin(); }
    const_iterator end() const { return preferences_.end(); }
    const_iterator cbegin() const { return preferences_.begin(); }
    const_iterator cend() const { return preferences_.end(); }

    preferences_t preferences_; //Publiczna, żeby PackageSender miał do niej dostęp w relacji kompozycji
    ProbabilityGenerator generator_;

    explicit ReceiverPreferences(ProbabilityGenerator pb = probability_generator) : generator_(std::move(pb)) {};
    void add_receiver(IPackageReceiver* r);
    void remove_receiver(IPackageReceiver* r);
    IPackageReceiver* choose_receiver();
    const preferences_t& get_preferences() const {return preferences_;};
};

class PackageSender{
public:
    ReceiverPreferences receiver_preferences_;
    PackageSender() : PackageBuffer_(std::nullopt){};
    PackageSender(PackageSender&&) = default;
    void send_package();
    const std::optional<Package>& get_sending_buffer() const {return PackageBuffer_;};

protected:
    void push_package(Package&& product) {PackageBuffer_ = Package(std::move(product));};
    std::optional<Package> PackageBuffer_;
