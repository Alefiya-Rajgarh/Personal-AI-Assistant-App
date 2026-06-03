import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../../../core/providers/auth_provider.dart';
import '../../../../core/widgets/aegis_button.dart';
import '../../../../core/widgets/aegis_text_field.dart';
import '../../../../core/theme/aegis_spacing.dart';

class RegisterScreen extends ConsumerWidget {
  const RegisterScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
      appBar: AppBar(title: const Text('Create account')),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(AssistanceSpacing.lg),
          child: Column(
            children: [
              const AegisTextField(
                label: 'Full name',
                hint: 'Alex Morgan',
                prefixIcon: Icons.person_outline,
              ),
              const SizedBox(height: AssistanceSpacing.md),
              const AegisTextField(
                label: 'Email',
                hint: 'you@company.com',
                prefixIcon: Icons.email_outlined,
              ),
              const SizedBox(height: AssistanceSpacing.md),
              const AegisTextField(
                label: 'Password',
                hint: '••••••••',
                prefixIcon: Icons.lock_outline,
                obscureText: true,
              ),
              const SizedBox(height: AssistanceSpacing.lg),
              AegisButton(
                label: 'Create account',
                onPressed: () {
                  ref.read(authStateProvider.notifier).state = true;
                  context.go('/home');
                },
              ),
              const SizedBox(height: AssistanceSpacing.md),
              TextButton(
                onPressed: () => context.go('/auth/login'),
                child: const Text('Already have an account? Sign in'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
