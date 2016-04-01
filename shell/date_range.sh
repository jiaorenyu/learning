start=$1
end=$2

echo $start
echo $end

start_sec=`date -d $start +%s`
end_sec=`date -d $end +%s`

cur_date=$start
cur_sec=`date -d $cur_date +%s`

while [ $cur_sec -le $end_sec ]
do
	echo $cur_date
	cur_date=`date -d "$cur_date +1 day" +%Y%m%d`
	cur_sec=`date -d $cur_date +%s`
done

