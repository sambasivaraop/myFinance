import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from './login.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'My Finance';
  public loginData = {};
  public userData;
  constructor(private _router: Router, private _loginservice: LoginService) { }

  getLoginDetails($event){
    this.loginData = $event;
    // console.log(typeof(localStorage.getItem('token')));
  }
  Isloggedin(){
    return (localStorage.getItem('token')) ? true : false;
  }
  onLogout(){
    this._loginservice.logout();
    this.loginData['token'] = null;
    // localStorage.removeItem('token');
  }

}
