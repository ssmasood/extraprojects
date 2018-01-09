#include "HashMap.hpp"

namespace
{

    unsigned int hash(const std::string& str){
        //Beszout's Identitiy
        unsigned int A = 5151;
        unsigned int B = 9299;
        unsigned int result = 33;
        for (unsigned int i = 0; i < str.length(); i++){
            result = (result * A) ^ (str[i] * B);
        }
        return result;
    }

}


//HashMap init constructors
HashMap::HashMap()
    : hasher{hash}, sz{0}, bCount{initialBucketCount}, buckets{new Node*[initialBucketCount]}
{
    this -> setNull();
}

HashMap::HashMap(HashFunction hasher)
    : hasher{hasher}, sz{0}, bCount{initialBucketCount}, buckets{new Node*[initialBucketCount]} 
{
    this -> setNull();
}

HashMap::HashMap(const HashMap& hm)
    : hasher{hm.hasher}, sz{0}, bCount{initialBucketCount}, buckets{new Node*[initialBucketCount]}
{
    this -> setNull();
}

HashMap::~HashMap()
{
    this -> delBuckets();
}

HashMap& HashMap::operator=(const HashMap& hm)
{
    if (&hm != this){
        this -> ~HashMap();
        hasher = hm.hasher;
        sz = hm.sz;
        bCount = hm.bCount;
        buckets = new Node*[hm.bCount];
        this -> setNull();
        copy(hm.buckets, buckets, hm.sz);
    }
    return *this;
}



//HashMap functions
void HashMap::add(const std::string& key, const std::string& value){
    if (contains(key))
        return;
    
    unsigned int index = hasher(key) % bCount;
    addTo(key, value, buckets[index]);
    sz++;
    
    if (loadFactor() > 0.8){
        unsigned int newBucketCount = bCount * 2 + 1;
        Node** newBuckets = new Node*[newBucketCount];
        setNull(newBuckets, newBucketCount);
        for (unsigned int i = 0; i < bCount; i++){
            Node* tempPtr = buckets[i];
            while (tempPtr != nullptr){
                index = hasher(tempPtr -> key) % newBucketCount;
                addTo(tempPtr -> key, tempPtr -> value, newBuckets[index]);
                tempPtr = tempPtr -> next;
            }
        }
        this -> ~HashMap();
        buckets = newBuckets;
        bCount = newBucketCount;
    }
    
    
}

void HashMap::remove(const std::string&key){
    if (!contains(key))
        return;

    unsigned int index = hasher(key) % bCount;
    Node* prev = buckets[index];
    Node* current = prev -> next;
    if (prev -> key == key){
        buckets[index] = current;
        delete prev;
    } else {
        while (current -> key != key){
            prev = current;
            current = prev -> next;
        }
        prev -> next = current -> next;
        delete current;
    }
    sz--;
}

bool HashMap::contains(const std::string& key) const{
    unsigned int index = hasher(key) % bCount;
    Node* tempPtr = buckets[index];
    while(tempPtr != nullptr){
        if (tempPtr -> key == key)
            return true;
        tempPtr = tempPtr -> next;
    }
    return false;
}

std::string HashMap::value(const std::string&key) const{
    if (this -> contains(key)){
        unsigned int index = hasher(key) % bCount;
        Node* tempPtr = buckets[index];
        while (tempPtr -> key != key)
            tempPtr = tempPtr -> next;
        return tempPtr -> value;
    }
    return "";
}

unsigned int HashMap::size() const{
    return sz;
}

unsigned int HashMap::bucketCount() const{
    return  bCount;
}

double HashMap::loadFactor() const{
    return (double) this -> size()/ this -> bucketCount();
}

unsigned int HashMap::maxBucketSize() const{
    unsigned int result = 0;
    unsigned int temp;
    for (unsigned int i = 0; i < bCount; i++){
        temp = 0;
        Node* tempPtr = buckets[i];
        while (tempPtr != nullptr){
            temp++;
            tempPtr = tempPtr -> next;
        }
        if (temp > result)
            result = temp;
        delete tempPtr;
    }
    return result;
}

void HashMap::clear(){
    this -> delBuckets();
    buckets = new Node*[bCount];
    sz = 0;
    this -> setNull();
}

//HashMap private functions

void HashMap::addTo(const std::string& key, const std::string& val, Node* &headPtr){
    Node* newNode = new Node;
    newNode -> key = key;
    newNode -> value = val;
    newNode -> next = headPtr;
    headPtr = newNode;
}

void HashMap::copy(Node** const &source, Node** target, unsigned int size){
    for (unsigned int i = 0; i < size; i++){
        Node* current = source[i];
        if (current != nullptr){
            target[i] = new Node;
            Node* temp = target[i];
            while (current != nullptr){
                temp -> key = current -> key;
                temp -> value = current -> value;
                if (current -> next != nullptr){
                    temp -> next = new Node;
                    temp = temp -> next;
                } else{
                    temp -> next = nullptr;
                }
                current = current -> next;
            }
        }
    }
}

void HashMap::setNull(){
    for (unsigned int i = 0; i < sz; i++){
        buckets[i] = nullptr;
    }
}

void HashMap::setNull(Node** &inBuckets, unsigned int size){
    for (unsigned int i = 0; i < size; i++){
        inBuckets[i] = nullptr;
    }
}

void HashMap::delBuckets(){
    for (unsigned int i = 0; i < bCount; i++){
        if (buckets[i] != nullptr){
            delNode(buckets[i]);
        }
    }
    delete[] buckets;
}

void HashMap::delNode(Node* source){
    if (source -> next != nullptr){
        delNode(source -> next);
    }
    delete source;
}
