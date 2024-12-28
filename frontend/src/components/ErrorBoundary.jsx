/* =========================================
   src/components/ErrorBoundary.jsx
   ========================================= */
   import React from 'react';

   class ErrorBoundary extends React.Component {
     constructor(props) {
       super(props);
       this.state = { hasError: false };
     }
   
     static getDerivedStateFromError(error) {
       // Update state to show fallback UI
       return { hasError: true };
     }
   
     componentDidCatch(error, errorInfo) {
       // Log error details
       console.error("ErrorBoundary caught an error:", error, errorInfo);
     }
   
     render() {
       if (this.state.hasError) {
         // Fallback UI
         return (
           <div style={{ textAlign: 'center', padding: '2rem' }}>
             <h2>Something went wrong.</h2>
             <p>Please try again later.</p>
           </div>
         );
       }
   
       return this.props.children; 
     }
   }
   
   export default ErrorBoundary;
   