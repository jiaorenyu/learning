tc qdisc del dev eth0 root

tc qdisc add dev eth0 root handle 1:0 htb default 10
tc class add dev eth0 parent 1: classid 1:1 htb rate 100mbps ceil 100mbps burst 100k
tc class add dev eth0 parent 1:1 classid 1:10 htb rate 30mbps ceil 30mbps
#for sgm
tc class add dev eth0 parent 1:1 classid 1:11 htb rate 2.5mbps ceil 2.5mbps
#for huawei
tc class add dev eth0 parent 1:1 classid 1:12 htb rate 2.5mbps ceil 2.5mbps

#for sgm
tc filter add dev eth0 protocol ip parent 1:0 prio 1 u32 match ip dst 114.141.129.197 flowid 1:11
tc filter add dev eth0 protocol ip parent 1:0 prio 1 u32 match ip dst 202.96.247.52 flowid 1:11
#for huawei
tc filter add dev eth0 protocol ip parent 1:0 prio 1 u32 match ip dst 119.145.15.155 flowid 1:12
