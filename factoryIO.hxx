#ifndef NETSIM_FACTORY_HPP
#define NETSIM_FACTORY_HPP
#include "types.hxx"
#include "nodes.hxx"

enum class State{
    VISITED,
    UNVISITED,
    VERYFIED
};

template<class Node>
class NodeCollection
{
public:
    using container_t = typename std::list<Node>;
    using iterator = typename container_t::iterator;
    using const_iterator = typename container_t::const_iterator;
    iterator begin() { return nodes_.begin(); }
    iterator end() { return nodes_.end(); }
    const_iterator cbegin() const { return nodes_.cbegin(); }
    const_iterator cend() const { return nodes_.cend(); }

    NodeCollection<Node>::iterator find_by_id( ElementID id){
        return std::find_if(nodes_.begin(),--nodes_.end(),[id](const auto& node){return node.get_id() == id;});
    }
    NodeCollection<Node>::const_iterator find_by_id( ElementID id) const{
        return std::find_if(nodes_.begin(),--nodes_.end(),[id](const auto& node){return node.get_id() == id;});
    }

    void add(Node&& node){
        nodes_.emplace_back(std::move(node));
        nodes_.sort(); //using defined "<" operator in ramp, worker, storehouse classes
    }
    bool remove_by_id(ElementID id) {
        bool if_removed_flag = false;
        const_iterator it = find_by_id(id);
        if (it->get_id() == id) {
            nodes_.erase(it);
            if_removed_flag = true;
        }
//        else
//            std::cout<<"Object to delete doesn't exist in collection - nothing changed"<<std::endl;
        return if_removed_flag;
    }

private:
    container_t nodes_;
};
