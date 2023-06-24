import React, { useEffect } from 'react';
import { Modal, Button, Text, Input, Row, Checkbox } from '@nextui-org/react';
import { Mail } from './Mail';
import { Password } from './Password';

export default function App() {
  const [visible, setVisible] = React.useState(true); //cambie el estado por defecto de visibilidad del modal a true
  const [user, setUser] = React.useState(''); //Contenido del campo email
  const [password, setPassword] = React.useState(''); //Contenido del campo password
  const [privateData, setPrivateData] = React.useState('');

  useEffect(() => {
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker
        .register('worker.js')
        .then((registration) => console.log('registration: ', registration));
    }
  }, []);

  const closeHandler = () => {
    setVisible(false);
    console.log('closed');
  };

  const clearTokenHandler = async () => {
    await navigator.serviceWorker.controller.postMessage({
      type: 'CLEAR_TOKEN',
      token: '',
    });
    setPrivateData('')
  }

  const privateHandler = async () => {
    const response = await fetch('http://localhost:8080/private', {
      method: 'GET',
      headers: {
        'Content-Type': 'text/html',
      },
    });
    if (response.ok) {
      const data = await response.text();
      setPrivateData(data);
    } else {
      setVisible(true);
    }
  };

  const loginHandler = async () => {
    //Handler para el login
    const response = await fetch('http://localhost:8080/login', {
      //Llamo al endpoint backend
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ user, password }),
    });
    if (response.ok) {
      const data = await response.json();
      console.log(data); //por el momento solo logueamos el token para ver que llego ok
      await navigator.serviceWorker.controller.postMessage({
        type: 'SET_TOKEN',
        token: data.token,
      });
      setVisible(false);
    } else {
      setUser('');
      setPassword('');
      console.log('Invalid credentials.');
    }
  };

  return (
    <div>
      {visible || (
        <div style={{display: 'flex'}}>
          <Button auto shadow onPress={privateHandler}>
            Show Data
          </Button>
          <Button auto shadow onPress={clearTokenHandler} color='error'>
            Clear token
          </Button>
        </div>
      )}
      <div>{privateData}</div>
      <Modal
        closeButton
        aria-labelledby='modal-title'
        open={visible}
        onClose={closeHandler}
      >
        <Modal.Header>
          <Text id='modal-title' size={18}>
            Welcome to
            <Text b size={18}>
              NextUI
            </Text>
          </Text>
        </Modal.Header>
        <Modal.Body>
          <Input
            clearable
            bordered
            fullWidth
            color='primary'
            size='lg'
            placeholder='User'
            value={user} //muestro lo que tengo en el estado
            onChange={(e) => setUser(e.target.value)} //actualizo el estado
            contentLeft={<Mail fill='currentColor' />}
          />
          <Input
            clearable
            bordered
            fullWidth
            color='primary'
            size='lg'
            placeholder='Password'
            type='password' //Pongo type password para que no muestre los caracteres
            value={password} //muestro lo que tengo en el estado
            onChange={(e) => setPassword(e.target.value)} //actualizo el estado
            contentLeft={<Password fill='currentColor' />}
          />
          <Row justify='space-between'>
            <Checkbox>
              <Text size={14}>Remember me</Text>
            </Checkbox>
            <Text size={14}>Forgot password?</Text>
          </Row>
        </Modal.Body>
        <Modal.Footer>
          <Button auto flat color='error' onPress={closeHandler}>
            Close
          </Button>
          <Button auto onPress={loginHandler}>
            Sign in
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}
