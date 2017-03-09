import L from 'leaflet';
import { GeoSearchControl, OpenStreetMapProvider } from 'leaflet-geosearch';

const provider = new OpenStreetMapProvider();

const searchControl = new GeoSearchControl({
  provider: provider,
});

const map = new L.Map('map');
map.addControl(searchControl);

new GeoSearchControl({
  provider: myProvider,           // required
  showMarker: true,               // optional: true|false  - default true
  showPopup: false,               // optional: true|false  - default false
  marker: {                       // optional: L.Marker    - default L.Icon.Default
    icon: new L.Icon.Default(),
    draggable: false,
  },
  maxMarkers: 1,                  // optional: number      - default 1
  retainZoomLevel: false,         // optional: true|false  - default false
  animateZoom: true,              // optional: true|false  - default true
});
