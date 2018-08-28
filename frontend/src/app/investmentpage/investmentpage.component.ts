import { Component, OnInit, Input } from '@angular/core';
import { Investment } from '../investment';
import { LoginService } from '../login.service';
import { InvestmentService} from '../investment.service';

@Component({
  selector: 'app-investmentpage',
  templateUrl: './investmentpage.component.html',
  styleUrls: ['./investmentpage.component.css']
})
export class InvestmentpageComponent implements OnInit {

  constructor(private _loginservice: LoginService, private _investmentservice: InvestmentService) { }
  public investModel;
  isRent = false;
  is80c = false;
  isInvestmentSelected = false;
  public errorMsg = '';
  public data;
  public error;
  public submitStatus = false;
  public existingDetails = [];

  ngOnInit() {
    this._loginservice.loginResponse
    .subscribe(
      data => {this.investModel = new Investment(JSON.parse(data).emp_id, '', '', '', '', '', '', '', ''); this.data = data},
      error => this.errorMsg = error.error,
      () =>     this._investmentservice.get_investment(JSON.parse(this.data)).subscribe(data => this.existingDetails = data),
  );
  }
  

  getInvestmentList() {
    return ['80C - Investment Under 80C',
      '80D - Medical Insurance',
      '80DD - Handicapped Dependant',
      '80E - Education Loan',
      '80U - Self with Physical Disability',
      '80EE - Additional Deduction on Home Loan Interest',
      'Interest on Housing Loan',
      'Rent',
      'Other Income',
      '80DDB - Medical Treatment',
      '80CCD - National Pension Scheme(NPS)',
      'Previous Employment']
  }
  get80CList() {
    return [
      'NSC/Tax Saving Bank Fixed deposits',
      'Public Provident Fund',
      'Insurance premium towards life',
      'Housing loan principal payment',
      'Sukanya Samriddhi A/c',
      'Tax saving MutualFunds',
      'ULIP',
      'Children Tuition Fee'
    ]
  }

  checkInvestment(value) {
    this.isInvestmentSelected = (value !== '' ? true : false);
    this.isRent = (value === 'Rent' ? true : false);
    this.is80c = (value === '80C - Investment Under 80C' ? true : false);
  }

  onSubmit(form){
    this._investmentservice.submit_investment(this.investModel)
    .subscribe(
          data => this.data = JSON.parse(JSON.stringify(data)),
          error => this.errorMsg = error.error,
          () => this.successfulSubmit(true, form),
        );
  }
  successfulSubmit(status, form){
    this.submitStatus = true;
    form.resetForm();
    this.ngOnInit();
    this.isRent = false;
    this.is80c = false;
    this.isInvestmentSelected = false;
  }
}
