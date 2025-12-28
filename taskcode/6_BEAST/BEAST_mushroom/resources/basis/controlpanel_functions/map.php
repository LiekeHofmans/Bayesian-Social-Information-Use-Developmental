<!DOCTYPE html>
<html>
<head>
    <title>Active participants</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../../pagination/assets/jquery-jvectormap-2.0.4.css" type="text/css" media="screen"/>
    <script src="../js_plugins/jquery-3.2.1.min.js"></script>
    <script src="../../pagination/assets/jquery-jvectormap-2.0.4.min.js"></script>
    <script src="../../pagination/assets/jquery-jvectormap-usa.js"></script>
    <script src="../../pagination/assets/jsquery-vectormap-india.js"></script>

</head>
<body>
<?php
include('../common.php');
require('../sqlLibrary.php');


$width = 800;
$height = $width * 2 / 3;
$query = "SELECT playerNr, location FROM  " . PROJECTID . "core WHERE location IS NOT NULL";
$conn = mysqli_connect(HOST, ADMIN, PASSW, DBNAME) or die(mysqli_error());
$result = mysqli_query($conn, $query) or die("Couldn't execute query " . $sql);;
$addresses = [];
while ($tables = mysqli_fetch_array($result)) {

    $addresses[$tables[0]] = $tables[1];


}


echo '<script>locali=' . json_encode($addresses) . ';</script>';
?>


<div id="europe-map" style="width: <?php echo $width; ?>px; height: <?php echo $height; ?>px"></div>
<script>
    $(function () {
        $('#europe-map').vectorMap({
            map: 'world_mill',
            scaleColors: ['#C8EEFF', '#0071A4'],
            normalizeFunction: 'polynomial',
            markerStyle: {
                initial: {
                    fill: '#F8E23B',
                    stroke: '#383f47'
                }
            },
            backgroundColor: '#383f47',
            markers: [],
            series: {
                markers: [{
                    values: []
                }]
            },
            regionStyle: {
                hover: {
                    "fill-opacity": 1
                }
            }

        });
    });


    $(document).ready(function () {

        map = $('#europe-map').vectorMap('get', 'mapObject');
        var i = 1;
        for (var id in locali) {

            var coordinates = locali[id];
            var both = coordinates.split('#');

            map.addMarker(i, {name: 'player ' + id, latLng: [parseFloat(both[0]), parseFloat(both[1])]})
            i++;


        }


    });

</script>


</body>
</html>
