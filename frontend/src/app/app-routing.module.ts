import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomepageComponent } from './homepage/homepage.component';
import { PayslipComponent } from './payslip/payslip.component';
import { LoginpageComponent } from './loginpage/loginpage.component';
import { InvestmentpageComponent } from './investmentpage/investmentpage.component';

const routes: Routes = [
    { path : 'homepage', component : HomepageComponent },
    { path : 'login', component : LoginpageComponent },
    { path : 'payslip', component : PayslipComponent },
    { path : 'investment', component : InvestmentpageComponent }
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [HomepageComponent, LoginpageComponent, PayslipComponent, InvestmentpageComponent]