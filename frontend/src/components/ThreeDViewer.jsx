import React from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, useTexture } from '@react-three/drei';

// A placeholder box geometry that uses a texture.
function My3DModel({ textureUrl }) {
  const texture = useTexture(textureUrl);
  return (
    <mesh rotation={[0.5, 1, 0]}>
      <boxGeometry args={[2, 2, 2]} />
      <meshStandardMaterial map={texture} />
    </mesh>
  );
}

function ThreeDViewer({ modelPath }) {
  return (
    <Canvas style={{ width: '100%', height: '400px' }}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[0, 5, 5]} />
      {/* Replace My3DModel with a real 3D model loader if you have one */}
      <My3DModel textureUrl={modelPath} />
      <OrbitControls />
    </Canvas>
  );
}

export default ThreeDViewer;
