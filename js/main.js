//Import the THREE.js library
import * as THREE from "https://cdn.skypack.dev/three@0.129.0/build/three.module.js";
// To allow for importing the .gltf file
import { GLTFLoader } from "https://cdn.skypack.dev/three@0.129.0/examples/jsm/loaders/GLTFLoader.js";
let object = null;
// Initialize Three.js scene
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setClearColor(0x000000, 0); // transparent
renderer.setSize(window.innerWidth, window.innerHeight);

document.getElementById("container3D").appendChild(renderer.domElement);

// Position the camera
camera.position.z = 22;
camera.position.y = -3;
camera.lookAt(new THREE.Vector3(0, -6, 0));

// Adding a directional light
var directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
directionalLight.position.set(0, 1, 1);
scene.add(directionalLight);

// Instantiate a loader for the .gltf file
const loader = new GLTFLoader();

// Load file
loader.load(
  'img/scene.gltf',
  function (gltf) {
    object = gltf.scene; 
    scene.add(gltf.scene);
    gltf.scene.scale.set(1, 1, 1);
  },
  function (xhr) {  // called while the model is loading
    console.log((xhr.loaded / xhr.total * 100) + '% loaded');
  },
  function (error) {
    console.error('An error happened while loading the model.', error);
  }
);

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    if (object) {
        object.rotation.y += 0.005;  // Rotates the object around the y-axis
    }
    renderer.render(scene, camera);
}
animate();