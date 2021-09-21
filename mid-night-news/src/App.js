import React from 'react';
import './App.css';
import Header from './components/headers/headers.component';
import EmailField from './components/email/email.components';

class App extends React.Component
{
  render()
  {
    return(
      <div style={{
        width : '100%',
        height : '100%'
      }}>
        <div style={{
        width : '100%',
        height : '30%'
      }}>
           <Header/>
        </div>
        <div style={{
        width : '100%',
        height : '70%'
      }}>
           <EmailField/>
        </div>
      </div>
      //add header
      
      //add body 
      //add footer
    );
  }
}
export default App;