import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InvestmentpageComponent } from './investmentpage.component';

describe('InvestmentpageComponent', () => {
  let component: InvestmentpageComponent;
  let fixture: ComponentFixture<InvestmentpageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InvestmentpageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InvestmentpageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
