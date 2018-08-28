import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Login } from './login';
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private _loginApi: string = 'http://localhost:8000/payroll/employee/login/';
  header = new HttpHeaders();
  public loginResponse;
  constructor(private _http: HttpClient) { }

  public appLogin(login: Login) {
    this.loginResponse =  this._http.post<any>(this._loginApi, login)
            .pipe(catchError(this.errorHandler))
    return this.loginResponse
  }

  public errorHandler(error: HttpErrorResponse) {
      return throwError(error);
  }

  public logout() {
    this.loginResponse = null;
    return true;
  }
}
