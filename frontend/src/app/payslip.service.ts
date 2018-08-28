import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { IPaySlip } from './payslip';
import { Observable } from 'rxjs/internal/Observable';


@Injectable({
  providedIn: 'root'
})
export class PayslipService {

  private _payslipApi: string = 'http://127.0.0.1:8000/payroll/payslip/employee_payslip_details/';
  headers = new HttpHeaders();
  constructor(private http: HttpClient) { }

  getSlip(data): Observable<IPaySlip[]>{
    this.headers = new HttpHeaders().set('Authorization', 'JWT '+data.token)
    return this.http.get<IPaySlip[]>(this._payslipApi, {headers: this.headers});
  }
}
