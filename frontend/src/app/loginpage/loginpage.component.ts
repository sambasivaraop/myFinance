import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { Login } from '../login';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-loginpage',
  templateUrl: './loginpage.component.html',
  styleUrls: ['./loginpage.component.css']
})
export class LoginpageComponent implements OnInit {

  constructor(private _loginservice: LoginService) { }

  ngOnInit() {
  }

  public errorMsg = '';
  public data;
  @Output() public loginEvent = new EventEmitter();
  loginModel = new Login('','');

  onSubmit()  {
    this._loginservice.appLogin(this.loginModel)
    .subscribe(
      data => {this.data = JSON.parse(data); localStorage.setItem('currentUser',JSON.stringify(this.data));},
      error => this.errorMsg = error.error,
      () => this.loginEvent.emit(this.data),
    );
  }
}
