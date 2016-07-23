#########################################################################
# File Name: all_in_one.sh
# Author: eipi10
# mail: gdzjydz@mail.ustc.edu.cn
# Created Time: Thu 21 Jul 2016 08:33:41 PM DST
#########################################################################
#!/bin/bash

AP_LB="loadbalanced>"
AP="stable_partition_removed>"
Naive="naive>"
file="../parconnect_SCC16/src/coloring/labelProp.hpp"

replace() {
        sed -i "s/"${AP_LB}"/"$1"/g" $file
        echo ${AP_LB}" to "$1
        sed -i "s/"${AP}"/"$1"/g" $file
        echo ${AP}" to "$1
        sed -i "s/"${Naive}"/"$1"/g" $file
        echo ${Naive}" to "$1
}

make_type() {
        if [ -d $1 ]; then
                rm -rf $1
        fi
        mkdir $1
        cd $1
        echo "building "$2
        replace $2
        cmake ../parconnect_SCC16
        make -j4
        cd ..
}

if [ ! -d "parconnect_SCC16" ]; then
        git clone --recursive https://github.com/cjain7/parconnect_SCC16.git
fi
echo "open the option BENCHMARK_ENABLE_CONN"

sed -i 's/OFF)/ON)/g' parconnect_SCC16/CMakeLists.txt

make_type Naive $Naive
make_type AP $AP
make_type AP_LB $AP_LB
