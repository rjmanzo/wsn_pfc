NodesPlaces = L.layerGroup()
        .addLayer(L.marker([ -32.029694,-60.653222 ])),
        .addLayer( L.marker([ -32.028944,-60.650055 ])),
        .addLayer(L.marker([ -32.028749,-60.649028 ])),
        .addLayer(L.marker([-32.035278,-60.649583])),
        .addTo(map);

L.control.layers(NodesPlaces).addTo(map);

L.layerControl.addOverlay(NodesPlaces, "NodesPlaces");

/*var sauzal = L.marker([-32.029694,-60.653222]).bindPopup('Clausula sauzal'),
    canutillar = L.marker([-32.028944,-60.650055]).addLayer(NodesLocation).bindPopup('Clausula canutillar'),
    verdolagal = L.marker([-32.028749,-60.649028]).addLayer(NodesLocation).bindPopup('Clausula verdolagal'),
    gramonal = L.marker([-32.035278,-60.649583]).addLayer(NodesLocation).bindPopup('Clausula gramonal');

var Locations = L.layerGroup([sauzal, canutillar, verdolagal, gramonal]).addLayer(NodesLocation);

layerControl.addOverlay(Locations , "");

/*var baseMaps = {
    "OpenStreetMap": OStreetMap,
    "Satellite": Satellite
};

var overlayMaps = {
    "Nodes": NodesLocation
};

L.control.layers(baseMaps, overlayMaps).addTo(map);*/
